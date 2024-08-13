angular
  .module("searchApp", [])
  .factory("Cart", function () {
    var items = [];
    return {
      getItems: function () {
        return items;
      },
      addArticle: function (article) {
        items.push(article);
      },
      removeItem: function (target) {
	items.splice(items.indexOf(target), 1);
      },
      sum: function () {
        return items.reduce(function (total, article) {
          return total + article.price;
        }, 0);
      }
    };
  })
  .factory("ArticleService", function($http) {
    var apiUrl = 'https://www.themealdb.com/api/json/v1/1/list.php?i=list';
    
    return {
      getArticles: function() {
        return $http.get(apiUrl)
          .then(function(response) {
            return response.data.meals.map(function(meal) {
              return {
                id: meal.idIngredient,
                name: meal.strIngredient,
                description: meal.strDescription || "No description available",
                price: Math.floor(Math.random() * 10) + 1
              };
            });
          });
      }
    };
  })
  .controller('ArticlesCtrl', function($scope, ArticleService, Cart) {
    $scope.cart = Cart;

    ArticleService.getArticles()
      .then(function(articles) {
        $scope.articles = articles;
      })
      .catch(function(error) {
        $scope.error = `Error fetching data: ${error.statusText}`;
      });
  })
  .controller("CartCtrl", function ($scope, Cart) {
    $scope.cart = Cart;
  });
