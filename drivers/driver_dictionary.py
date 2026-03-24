STANDARD_DRIVERS = {
    "Compute_Time": [
        "ec2_hours",
        "lambda_duration_gb_seconds",
        "fargate_hours"
    ],
    "Request_Count": [
        "lambda_invocations",
        "api_requests"
    ],
    "Capacity_Units": [
        "dynamodb_rcu",
        "dynamodb_wcu"
    ],
    "Storage_Volume": [
        "s3_gb",
        "ebs_gb",
        "rds_storage_gb"
    ],
    "Throughput": [
        "data_transfer_gb",
        "nat_gateway_gb"
    ],
    "IO_Performance": [
        "iops",
        "read_ops",
        "write_ops"
    ]
}
