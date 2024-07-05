import sys
import mysql.connector
from mysql.connector import Error
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, qApp, QLabel, QVBoxLayout, QWidget, QPushButton, \
    QLineEdit, QMessageBox, QTableWidget, QTableWidgetItem, QGridLayout, QHBoxLayout, QGroupBox, QTextEdit, QComboBox, \
    QDateEdit, QDateTimeEdit, QTimeEdit, QSpinBox, QDoubleSpinBox, QFormLayout, QDialog, QHeaderView


# Establish a connection to the MySQL database
def create_connection(host_name, user_name, user_password, db_name):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password,
            database=db_name
        )
        print("Connection to MySQL DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")
    return connection


# Replace with your own database credentials
host_name = "localhost"
user_name = "root"
user_password = "jj1995123"
db_name = "fiker_decor"

connection = create_connection(host_name, user_name, user_password, db_name)


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


# PyQt5 Main Window
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Decor Company Management System')

        # Create menu bar
        menubar = self.menuBar()
        fileMenu = menubar.addMenu('File')

        # Add actions to menu bar
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

        # Task and Schedule Management Action
        taskManagementAction = QAction('Task and Schedule Management', self)
        taskManagementAction.triggered.connect(self.task_management)
        menubar.addAction(taskManagementAction)

        # Reporting and Analytics Action
        reportingAction = QAction('Reporting and Analytics', self)
        reportingAction.triggered.connect(self.reporting_analytics)
        menubar.addAction(reportingAction)

        # Central Widget and Layout
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout(self.central_widget)

        self.label = QLabel("Welcome to the Decor Company Management System")
        self.layout.addWidget(self.label)

    def user_management(self):
        self.clear_layout(self.layout)

        # Add User Management widgets
        group_box = QGroupBox("User Management")
        layout = QVBoxLayout()

        # Example: Add buttons or fields for user management
        layout.addWidget(QLabel("User Management Section"))
        layout.addWidget(QPushButton("Add User"))
        layout.addWidget(QPushButton("Update User"))
        layout.addWidget(QPushButton("Delete User"))

        group_box.setLayout(layout)
        self.layout.addWidget(group_box)

    def inventory_management(self):
        self.clear_layout(self.layout)

        # Add Inventory Management widgets
        group_box = QGroupBox("Inventory Management")
        layout = QVBoxLayout()

        # Example: Add buttons or fields for inventory management
        layout.addWidget(QLabel("Inventory Management Section"))
        layout.addWidget(QPushButton("Add Product"))
        layout.addWidget(QPushButton("Update Product"))
        layout.addWidget(QPushButton("Delete Product"))

        group_box.setLayout(layout)
        self.layout.addWidget(group_box)

    def order_management(self):
        self.clear_layout(self.layout)

        # Add Order Management widgets
        group_box = QGroupBox("Order Management")
        layout = QVBoxLayout()

        # Example: Add buttons or fields for order management
        layout.addWidget(QLabel("Order Management Section"))
        layout.addWidget(QPushButton("Create Order"))
        layout.addWidget(QPushButton("Update Order"))
        layout.addWidget(QPushButton("Cancel Order"))

        group_box.setLayout(layout)
        self.layout.addWidget(group_box)

    def customer_management(self):
        self.clear_layout(self.layout)

        # Add Customer Management widgets
        group_box = QGroupBox("Customer Management")
        layout = QVBoxLayout()

        # Example: Add buttons or fields for customer management
        layout.addWidget(QLabel("Customer Management Section"))
        layout.addWidget(QPushButton("Add Customer"))
        layout.addWidget(QPushButton("Update Customer"))
        layout.addWidget(QPushButton("Delete Customer"))

        group_box.setLayout(layout)
        self.layout.addWidget(group_box)

    def financial_management(self):
        self.clear_layout(self.layout)

        # Add Financial Management widgets
        group_box = QGroupBox("Financial Management")
        layout = QVBoxLayout()

        # Example: Add buttons or fields for financial management
        layout.addWidget(QLabel("Financial Management Section"))
        layout.addWidget(QPushButton("Generate Invoice"))
        layout.addWidget(QPushButton("Record Payment"))
        layout.addWidget(QPushButton("View Reports"))

        group_box.setLayout(layout)
        self.layout.addWidget(group_box)

    def task_management(self):
        self.clear_layout(self.layout)

        # Add Task and Schedule Management widgets
        group_box = QGroupBox("Task and Schedule Management")
        layout = QVBoxLayout()

        # Example: Add buttons or fields for task management
        layout.addWidget(QLabel("Task and Schedule Management Section"))
        layout.addWidget(QPushButton("Schedule Event"))
        layout.addWidget(QPushButton("Assign Task"))
        layout.addWidget(QPushButton("View Calendar"))

        group_box.setLayout(layout)
        self.layout.addWidget(group_box)

    def reporting_analytics(self):
        self.clear_layout(self.layout)

        # Add Reporting and Analytics widgets
        group_box = QGroupBox("Reporting and Analytics")
        layout = QVBoxLayout()

        # Example: Add buttons or fields for reporting and analytics
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


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())
