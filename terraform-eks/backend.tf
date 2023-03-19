terraform {
  backend "s3" {
    bucket = "rajexambuc"
    key    = "terraform.tfstate"
    region = "us-east-2"
  }
}