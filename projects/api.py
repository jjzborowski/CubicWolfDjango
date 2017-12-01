from projects.views import ProjectViewSet


ProjectAPI = {
    'list': ProjectViewSet.as_view({
        'get': 'list',
        'post': 'create'
    }),
    'detail': ProjectViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'patch': 'partial_update',
        'delete': 'destroy'
    })
}
