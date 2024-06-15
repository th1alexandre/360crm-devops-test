resource "aws_dynamodb_table" "table" {
  name           = var.table_name
  read_capacity  = "5"
  write_capacity = "5"
  hash_key       = "logID"

  point_in_time_recovery {
    enabled = var.point_in_time_recovery
  }

  attribute {
    name = "logID"
    type = "S"
  }
}
