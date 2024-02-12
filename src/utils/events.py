def on_additional_arguments(parser):
    args = parser.add_argument_group('Additional arguments')
    args.add_argument(
        '--wait-time-min', type=float, default=5.0, help='Min time between tasks', env_var='LOCUST_WAIT_TIME_MIN'
    )
    args.add_argument(
        '--wait-time-max', type=float, default=10.0, help='Max time between tasks', env_var='LOCUST_WAIT_TIME_MAX'
    )
