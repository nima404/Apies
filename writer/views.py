from rest_framework import generics, viewsets, views, mixins, status, permissions


class UserDetail(viewsets.GenericViewSet, mixins.UpdateModelMixin):
    serializer_class = ...
    queryset = ...
    permission_classes = [
        # permissions.IsAuthenticated  # TODO: uncomment permissions
    ]
