import sys
import mysql.connector
from mysql.connector import Error
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, qApp, QLabel, QVBoxLayout, QWidget, QPushButton, QLineEdit, QMessageBox, QTableWidget, QTableWidgetItem

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
db_name ="fiker_decor"

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

        userManagementAction = QAction('User Management', self)
        userManagementAction.triggered.connect(self.user_management)
        menubar.addAction(userManagementAction)

        inventoryManagementAction = QAction('Inventory Management', self)
        inventoryManagementAction.triggered.connect(self.inventory_management)
        menubar.addAction(inventoryManagementAction)

        # Main layout
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout(self.central_widget)

        self.label = QLabel("Welcome to the Decor Company Management System")
        self.layout.addWidget(self.label)

    def user_management(self):
        self.label.setText("User Management Section")
        self.show_user_management()

    def inventory_management(self):
        self.label.setText("Inventory Management Section")

    def show_user_management(self):
        self.clear_layout(self.layout)

        add_user_label = QLabel("Add New User")
        self.layout.addWidget(add_user_label)

        self.username_input = QLineEdit(self)
        self.username_input.setPlaceholderText("Username")
        self.layout.addWidget(self.username_input)

        self.password_input = QLineEdit(self)
        self.password_input.setPlaceholderText("Password")
        self.password_input.setEchoMode(QLineEdit.Password)
        self.layout.addWidget(self.password_input)

        self.role_input = QLineEdit(self)
        self.role_input.setPlaceholderText("Role (admin/employee)")
        self.layout.addWidget(self.role_input)

        add_user_button = QPushButton("Add User", self)
        add_user_button.clicked.connect(self.add_user)
        self.layout.addWidget(add_user_button)

        show_users_button = QPushButton("Show Users", self)
        show_users_button.clicked.connect(self.show_users)
        self.layout.addWidget(show_users_button)

        self.user_table = QTableWidget(self)
        self.layout.addWidget(self.user_table)

    def add_user(self):
        username = self.username_input.text()
        password = self.password_input.text()
        role = self.role_input.text()

        if username and password and role:
            add_user_query = """
            INSERT INTO users (username, password, role) VALUES (%s, %s, %s)
            """
            new_user = (username, password, role)
            execute_query(connection, add_user_query, new_user)
            QMessageBox.information(self, "Success", "User added successfully")
        else:
            QMessageBox.warning(self, "Error", "Please fill in all fields")

    def show_users(self):
        self.user_table.clear()
        self.user_table.setRowCount(0)
        self.user_table.setColumnCount(3)
        self.user_table.setHorizontalHeaderLabels(["ID", "Username", "Role"])

        select_users_query = "SELECT id, username, role FROM users"
        users = execute_read_query(connection, select_users_query)

        for row_number, row_data in enumerate(users):
            self.user_table.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.user_table.setItem(row_number, column_number, QTableWidgetItem(str(data)))

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
