# Databricks notebook source
# MAGIC %md
# MAGIC | **GPU Model** | **VRAM Capacity** | **Memory Type**         |
# MAGIC |---------------|-------------------|-------------------------|
# MAGIC | **T4**        | 16GB              | GDDR6                   |
# MAGIC | **A10G**      | 24GB              | GDDR6                   |
# MAGIC | **V100**      | 32GB              | HBM2 (High Bandwidth Memory) |
# MAGIC | **A100**      | 40GB or 80GB      | HBM2                    |
# MAGIC | **L4**         | 24GB              | GDDR6                   |
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC Based on the tests, the minimal node configurations for each model size are:

# COMMAND ----------

# MAGIC %md
# MAGIC | Model Size | Minimal Node Configuration | Cost | Latency |
# MAGIC |---------------|----------|----------|----------|
# MAGIC | 0.5B     | g4dn.xlarge[T4]  |0.71 dbu/h  | 6s  |
# MAGIC | 1.5B     | g4dn.xlarge[T4]  |0.71 dbu/h  | 5s  |
# MAGIC | 3B       | g4dn.xlarge[T4]  |0.71 dbu/h  | 8s  |
# MAGIC | 7B       | g4dn.2xlarge[T4]  |1.43 dbu/h  | 136s  |
# MAGIC | 14B      | g5.12xlarge[A10G]  |7.69 dbu/h  | 15s |
# MAGIC | 32B      | g5.12xlarge[A10G] |7.69 dbu/h  | 30s |
# MAGIC | 72B      | p4d.24xlarge[A100] | 44.45 dbu/h | * |
# MAGIC
# MAGIC \* couldn't find instances to allocate
