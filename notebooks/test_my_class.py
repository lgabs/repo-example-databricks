# Databricks notebook source
# MAGIC %md 
# MAGIC 
# MAGIC - testar aqui no databricks seus notebooks
# MAGIC - criar um repo no github
# MAGIC - criar um token no github
# MAGIC - add o token aqui no databricks
# MAGIC - "linkar" um notebook ao repositório da sua conta com token adicionado
# MAGIC - commitar em branch, abrir PR
# MAGIC 
# MAGIC documentação: https://docs.databricks.com/notebooks/github-version-control.html

# COMMAND ----------

# MAGIC %run ./my_class

# COMMAND ----------

my_cool_class = MyClass()

my_cool_class

# COMMAND ----------

my_cool_class.f()