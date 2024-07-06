import sys
import mysql.connector
from mysql.connector import Error
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, qApp, QLabel, QVBoxLayout, QWidget, QPushButton, \
    QLineEdit, QMessageBox, QGroupBox, QHBoxLayout, QComboBox, QFormLayout, QDialog, QTableWidget, QTableWidgetItem, \
    QHeaderView, QFileDialog, QTextEdit
from PyQt5.QtGui import QFont, QPixmap
from PyQt5.QtCore import Qt


# Establish a connection to the MySQL database
def create_connection(localhost, root, jj1995123, fiker_decor):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=localhost,
            user=root,
            passwd=jj1995123,
            database=fiker_decor
        )
        print("Connection to MySQL DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")
    return connection


# Function to execute SQL queries
def execute_query(connection, query, data=None):
    cursor = connection.cursor()
    try:
        if data:
            cursor.execute(query, data)
        else:
            cursor.execute(query)
        connection.commit()
        print("Query executed successfully")
    except Error as e:
        print(f"The error '{e}' occurred")


# Function to read data from the database
def execute_read_query(connection, query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as e:
        print(f"The error '{e}' occurred")


# Main Window with Login and Role Selection
class LoginWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Fiker Decor Banking System')
        self.setGeometry(200, 200, 400, 300)

        layout = QVBoxLayout()

        self.label = QLabel("Login to Fiker Decor Banking System")
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setFont(QFont('Arial', 14))
        layout.addWidget(self.label)

        self.role_label = QLabel("Select Role:")
        self.role_label.setAlignment(Qt.AlignCenter)
        self.role_label.setFont(QFont('Arial', 12))
        layout.addWidget(self.role_label)

        self.role_combo = QComboBox()
        self.role_combo.addItems(["Admin", "Shop Cashier", "Inventory Personnel"])
        layout.addWidget(self.role_combo)

        self.password_label = QLabel("Enter Password:")
        self.password_label.setAlignment(Qt.AlignCenter)
        self.password_label.setFont(QFont('Arial', 12))
        layout.addWidget(self.password_label)

        self.password_input = QLineEdit()
        self.password_input.setEchoMode(QLineEdit.Password)
        layout.addWidget(self.password_input)

        self.login_button = QPushButton("Login")
        self.login_button.clicked.connect(self.login)
        self.login_button.setFont(QFont('Arial', 12))
        layout.addWidget(self.login_button)

        self.setLayout(layout)

    def login(self):
        role = self.role_combo.currentText()
        password = self.password_input.text()

        # Define passwords for each role
        admin_password = "admin123"
        cashier_password = "cashier123"
        inventory_password = "inventory123"

        # Validate password based on selected role
        if role == "Admin" and password == admin_password:
            self.admin_window = AdminWindow()
            self.admin_window.show()
            self.close()
        elif role == "Shop Cashier" and password == cashier_password:
            self.cashier_window = CashierWindow()
            self.cashier_window.show()
            self.close()
        elif role == "Inventory Personnel" and password == inventory_password:
            self.inventory_window = InventoryWindow()
            self.inventory_window.show()
            self.close()
        else:
            QMessageBox.warning(self, "Login Failed", "Invalid credentials. Please try again.")


# Admin Window
class AdminWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Admin - Fiker Decor Banking System')
        self.setGeometry(100, 100, 800, 600)

        # Menu Bar
        menubar = self.menuBar()
        fileMenu = menubar.addMenu('File')
        exitAction = QAction('Exit', self)
        exitAction.triggered.connect(qApp.quit)
        fileMenu.addAction(exitAction)

        # User Management Action
        userManagementAction = QAction('User Management', self)
        userManagementAction.triggered.connect(self.user_management)
        menubar.addAction(userManagementAction)

        # Inventory Management Action
        inventoryManagementAction = QAction('Inventory Management', self)
        inventoryManagementAction.triggered.connect(self.inventory_management)
        menubar.addAction(inventoryManagementAction)

        # Order Management Action
        orderManagementAction = QAction('Order Management', self)
        orderManagementAction.triggered.connect(self.order_management)
        menubar.addAction(orderManagementAction)

        # Customer Management Action
        customerManagementAction = QAction('Customer Management', self)
        customerManagementAction.triggered.connect(self.customer_management)
        menubar.addAction(customerManagementAction)

        # Financial Management Action
        financialManagementAction = QAction('Financial Management', self)
        financialManagementAction.triggered.connect(self.financial_management)
        menubar.addAction(financialManagementAction)

        # Task Management Action
        taskManagementAction = QAction('Task Management', self)
        taskManagementAction.triggered.connect(self.task_management)
        menubar.addAction(taskManagementAction)

        # Reporting and Analytics Action
        reportingAction = QAction('Reporting and Analytics', self)
        reportingAction.triggered.connect(self.reporting_analytics)
        menubar.addAction(reportingAction)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout(self.central_widget)

        self.label = QLabel("Welcome Admin! Choose a management section from the menu.")
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setFont(QFont('Arial', 14))
        self.layout.addWidget(self.label)

    def user_management(self):
        self.clear_layout(self.layout)

        group_box = QGroupBox("User Management")
        layout = QVBoxLayout()

        layout.addWidget(QLabel("User Management Section"))
        layout.addWidget(QPushButton("Add User"))
        layout.addWidget(QPushButton("Update User"))
        layout.addWidget(QPushButton("Delete User"))

        group_box.setLayout(layout)
        self.layout.addWidget(group_box)

    def inventory_management(self):
        self.clear_layout(self.layout)

        group_box = QGroupBox("Inventory Management")
        layout = QVBoxLayout()

        layout.addWidget(QLabel("Inventory Management Section"))
        layout.addWidget(QPushButton("Add Product"))
        layout.addWidget(QPushButton("Update Product"))
        layout.addWidget(QPushButton("Delete Product"))

        group_box.setLayout(layout)
        self.layout.addWidget(group_box)

    def order_management(self):
        self.clear_layout(self.layout)

        group_box = QGroupBox("Order Management")
        layout = QVBoxLayout()

        layout.addWidget(QLabel("Order Management Section"))
        layout.addWidget(QPushButton("Create Order"))
        layout.addWidget(QPushButton("Update Order"))
        layout.addWidget(QPushButton("Cancel Order"))

        group_box.setLayout(layout)
        self.layout.addWidget(group_box)

    def customer_management(self):
        self.clear_layout(self.layout)

        group_box = QGroupBox("Customer Management")
        layout = QVBoxLayout()

        layout.addWidget(QLabel("Customer Management Section"))
        layout.addWidget(QPushButton("Add Customer"))
        layout.addWidget(QPushButton("Update Customer"))
        layout.addWidget(QPushButton("Delete Customer"))

        group_box.setLayout(layout)
        self.layout.addWidget(group_box)

    def financial_management(self):
        self.clear_layout(self.layout)

        group_box = QGroupBox("Financial Management")
        layout = QVBoxLayout()

        layout.addWidget(QLabel("Financial Management Section"))
        layout.addWidget(QPushButton("Generate Invoice"))
        layout.addWidget(QPushButton("Record Payment"))
        layout.addWidget(QPushButton("View Reports"))

        group_box.setLayout(layout)
        self.layout.addWidget(group_box)

    def task_management(self):
        self.clear_layout(self.layout)

        group_box = QGroupBox("Task Management")
        layout = QVBoxLayout()

        layout.addWidget(QLabel("Task Management Section"))
        layout.addWidget(QPushButton("Schedule Task"))
        layout.addWidget(QPushButton("Assign Task"))
        layout.addWidget(QPushButton("View Calendar"))

        group_box.setLayout(layout)
        self.layout.addWidget(group_box)

    def reporting_analytics(self):
        self.clear_layout(self.layout)

        group_box = QGroupBox("Reporting and Analytics")
        layout = QVBoxLayout()

        layout.addWidget(QLabel("Reporting and Analytics Section"))
        layout.addWidget(QPushButton("Generate Sales Report"))
        layout.addWidget(QPushButton("View Inventory Report"))
        layout.addWidget(QPushButton("Customer Insights"))

        group_box.setLayout(layout)
        self.layout.addWidget(group_box)

    def clear_layout(self, layout):
        while layout.count():
            child = layout.takeAt(0)
            if child.widget():
                child.widget().deleteLater()


# Shop Cashier Window
class CashierWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Shop Cashier - Fiker Decor Banking System')
        self.setGeometry(100, 100, 800, 600)

        layout = QVBoxLayout()

        self.label = QLabel("Welcome Shop Cashier! This area is under development.")
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setFont(QFont('Arial', 14))
        layout.addWidget(self.label)

        self.setLayout(layout)


# Inventory Personnel Window
class InventoryWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Inventory Personnel - Fiker Decor Banking System')
        self.setGeometry(100, 100, 800, 600)

        layout = QVBoxLayout()

        self.label = QLabel("Welcome Inventory Personnel! This area is under development.")
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setFont(QFont('Arial', 14))
        layout.addWidget(self.label)

        self.setLayout(layout)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    connection = create_connection("localhost", "root", "jj1995123", "fiker_decor")

    if connection:
        print("Connection successfully established.")
        login_window = LoginWindow()
        login_window.show()
        sys.exit(app.exec_())
    else:
        print("Connection could not be established.")
