from courses.views import CoursesViewSet


CourseAPI = {
    'list': CoursesViewSet.as_view({
        'get': 'list',
        'post': 'create'
    }),
    'detail': CoursesViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'patch': 'partial_update',
        'delete': 'destroy'
    })
}
