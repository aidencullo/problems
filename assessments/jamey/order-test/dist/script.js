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
  .controller('ArticlesCtrl', function($scope, $http, Cart) {
    $scope.cart = Cart;
    const apiUrl = 'https://www.themealdb.com/api/json/v1/1/list.php?i=list'; // Replace with your API URL

    $http.get(apiUrl)
      .then(function(response) {
	$scope.articles = response.data.meals.map((meal) => {
	  return {
	    id: meal.idIngredient,
	    name: meal.strIngredient,
	    description: meal.strDescription,
	    price: Math.floor(Math.random() * 10) + 1
	  };
	})
      })
      .catch(function(error) {
        $scope.error = `Error fetching data: ${error.statusText}`;
      });
  })
  .controller("CartCtrl", function ($scope, Cart) {
    $scope.cart = Cart;
  });
