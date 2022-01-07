from rest_framework import serializers
from .models import *

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','username','email','password','address','phone','create_at']

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id','title','description','storeId','category','price','thumbnail','stock','condition','rating','create_at']

class ProductImgSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImg
        fields = ['id','productId','url']


class StoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Store
        fields = ['id','userId','name','create_at']

class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = ['id','userId','quantity']


class CartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = ['id','cartId','productId','quantity','create_at']

class FileUploadSerializer(serializers.ModelSerializer):
    class Meta:
        model = FileUpload
        fields = ['imgFile']

class JoinSerializer(serializers.ModelSerializer):
    product_details = ProductSerializer(source='productId')
    class Meta:
        model = CartItem
        fields = ['id','cartId','productId','quantity','product_details','create_at']