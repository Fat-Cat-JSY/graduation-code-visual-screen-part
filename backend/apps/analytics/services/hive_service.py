# coding: utf-8

from pyspark.sql import SparkSession
from backend.graduation_project.settings import dbName
from scripts.convert_mysql_to_hive import ConvertMySQLToHive


def hive_func(sql_list: list):
    cv = ConvertMySQLToHive(dbName)
    for sql_str in sql_list:
        hive_list = cv.convert_mysql_to_hive(sql_str)
        if len(hive_list) > 0:
            hive_execute(hive_list)


def hive_execute(hive_list: list):
    """
    使用Spark SQL替代HS2执行HiveQL
    """
    try:
        spark = SparkSession.builder \
            .appName("HiveOperations") \
            .config("spark.sql.warehouse.dir", "/user/hive/warehouse") \
            .config("hive.metastore.uris", "thrift://192.168.64.101:9083") \
            .enableHiveSupport() \
            .master("spark://192.168.64.101:7077") \
            .getOrCreate()

        for hive_sql in hive_list:
            try:
                spark.sql(hive_sql)
                print(f"执行成功: {hive_sql}")
            except Exception as e:
                print(f"Exception======> {e}")
                print(f"hive_sql=====> {hive_sql}")

        spark.stop()
    except Exception as e:
        print(f"SparkSession初始化失败: {e}")
        return