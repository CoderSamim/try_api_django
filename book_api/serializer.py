from rest_framework import serializers

from book_api.models import Book

# class BookSerializer(serializers.Serializer):
#     id=serializers.IntegerField(read_only=True)
#     title=serializers.CharField()
#     number_of_pages=serializers.IntegerField()
#     publish_date=serializers.DateField()
#     quantity=serializers.IntegerField()
    
#     def create(self,data):
#         return Book.objects.create(**data)
    
#     def update(self,instance,data):
#         instance.title=data.get('title',instance.title)
#         instance.number_of_pages=data.get('number_of_pages',instance.number_of_pages)
#         instance.publish_date=data.get('publish_date',instance.publish_date)
#         instance.quantity=data.get('quantity',instance.quantity)
        
#         instance.save()
#         return instance


from django.forms import ValidationError

class BookSerializer(serializers.ModelSerializer):
    description=serializers.SerializerMethodField()
    class Meta:
        model=Book
        fields="__all__"
        
    def validate_title(self,value):
        if value=="do or die":
            raise ValidationError("you can't add this title")
        return value
    
    def validate(self,data):
        if data["number_of_pages"] > 200 and data["quantity"] > 200 :
            raise ValidationError("to heavy to inventory")
        return data
    
    def get_description(self,data):     #get_   ---compulsory and then name
        return "this book's name is "+ data.title + "and it is "+ str(data.number_of_pages)+" pages long."
    
