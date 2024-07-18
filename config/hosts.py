from django_hosts import patterns, host

host_patterns = patterns(
    "",
    host("api", "config.urls.api", name="api"),
    host("admin", "config.urls.admin", name="admin"),
)