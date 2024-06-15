module "s3" {
  source = "./modules/s3"

  count = var.s3_enabled ? 1 : 0

  bucket_name = var.bucket_name
  bucket_acl  = var.bucket_acl

  log_bucket_name = var.log_bucket_name
  log_bucket_acl  = var.log_bucket_acl
}

module "dynamo" {
  source = "./modules/dynamodb"

  count = var.dynamodb_enabled ? 1 : 0

  table_name             = var.table_name
  point_in_time_recovery = var.point_in_time_recovery
}
