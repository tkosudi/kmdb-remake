from accounts.serializers import UserSerializer
from rest_framework import serializers
from .models import Movie, Genre, Review
from accounts.serializers import CriticSerializer
import ipdb

class ReviewSerializer(serializers.ModelSerializer):
    critic = CriticSerializer(read_only=True)
    class Meta:
        model = Review
        fields = '__all__'
        extra_kwargs = {'movie': {'write_only': True}}

class CriticReviewSerializer(serializers.ModelSerializer):
    critic = CriticSerializer(read_only=True)
    class Meta:
        model = Review
        fields = '__all__'

    def create(self, validated_data):
        ipdb.set_trace()

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ['id', 'name']

class MovieSerializer(serializers.ModelSerializer):
    genres = GenreSerializer(many=True)

    class Meta:
        model = Movie
        fields = '__all__'

    def create(self, validated_data):
        genres_data = validated_data.pop('genres') # Faz a retirada dos generos para serem tratados a parte
        movie = Movie.objects.get_or_create(**validated_data)[0] # Cria o filme na model

        for genre in genres_data: # Iteração sobre "genres_data"
            gen = Genre.objects.get_or_create(**genre)[0] # Pegando ou criando o gênero em questão
            movie.genres.add(gen) # Adicionando o genre ao movie, como se fosse um append 

        return movie


class FullMovieSerializer(serializers.ModelSerializer):
    genres = GenreSerializer(many=True)
    reviews = ReviewSerializer(many=True)
    class Meta:
        model = Movie
        fields = '__all__'
