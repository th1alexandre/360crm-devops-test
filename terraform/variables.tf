# dynamoDB
variable "dynamodb_enabled" {}
variable "table_name" {}
variable "point_in_time_recovery" {}

# s3
variable "s3_enabled" {}
variable "s3_force_path_style" {}

variable "bucket_name" {}
variable "bucket_acl" {}

variable "log_bucket_name" {}
variable "log_bucket_acl" {}
