from rest_framework import serializers
from restaurants.models import Restaurant


class RestaurantListSerializer(serializers.ModelSerializer):

    detailView = serializers.HyperlinkedIdentityField(
        view_name='api-detail',
        lookup_field="id",
        lookup_url_kwarg="restaurant_id"
    )

    updateView = serializers.HyperlinkedIdentityField(
        view_name='api-update',
        lookup_field="id",
        lookup_url_kwarg="restaurant_id"
    )

    deleteView = serializers.HyperlinkedIdentityField(
        view_name='api-delete',
        lookup_field="id",
        lookup_url_kwarg="restaurant_id"
    )

    class Meta:
        model = Restaurant
        fields = [
            'name',
            'opening_time',
            'closing_time',
            'detailView',
            'updateView',
            'deleteView',
        ]


class RestaurantDetailSerializer(serializers.ModelSerializer):
    updateView = serializers.HyperlinkedIdentityField(
        view_name='api-update',
        lookup_field="id",
        lookup_url_kwarg="restaurant_id"
    )

    deleteView = serializers.HyperlinkedIdentityField(
        view_name='api-delete',
        lookup_field="id",
        lookup_url_kwarg="restaurant_id"
    )

    class Meta:
        model = Restaurant
        fields = [
            'id',
            'owner',
            'name',
            'description',
            'opening_time',
            'closing_time',
            'updateView',
            'deleteView',
        ]


class RestaurantCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = [
            'name',
            'description',
            'opening_time',
            'closing_time',
        ]
