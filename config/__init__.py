import pymysql

# mysqlclient 대신 PyMySQL 사용 (Django가 요구하는 mysqlclient 버전 체크 통과용)
pymysql.version_info = (2, 2, 1, "final", 0)
pymysql.install_as_MySQLdb()
