# Create a dictionary with the service categories as keys and the services as values
services_dict = {
    'compute': ['EC2', 'lambda', 'fargate', 'outposts', 'lightsail', 'batch'],
    'storage': ['s3', 'ebs', 'efs', 'storage gateway', 'backup'],
    'content delivery': ['cloud front', 'global accelerator', 's3 transfer acceleration'],
    'networking': ['route53', 'virtual private cloud(vpc)', 'direct connect', 'virtual private network(vpn)',
                   'api gateway'],
    'database': ['relational database service(rds)', 'aurora', 'dynamoDB', 'documentDB', 'elasti-cache', 'neptune'],
    'migration and transfer': ['database migration service(dms)', 'server migration service(sms)', 'snow family',
                               'datasync'],
    'analytics': ['redshift', 'athena', 'glue', 'kinesis', 'elastic map reduce(emr)', 'data pipeline'],
    'machine learning': ['rekognition', 'comprehend', 'polly', 'sage maker', 'translate', 'lex'],
    'developer tools': ['cloud9', 'code commit', 'code build', 'code deploy', 'code pipeline', 'x-ray'],
    'deployment and infrastructure management': ['cloud formation', 'elastic beanstalk', 'opsworks'],
    'messaging and integration': ['simple queue service(sqs)', 'simple notification service(sns)',
                                  'simple email service(ses)'],
    'auditing monitoring and logging': ['cloud watch', 'cloud trail']
}


