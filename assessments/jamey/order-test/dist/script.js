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
  .controller("ArticlesCtrl", function ($scope, Cart) {
    $scope.cart = Cart;
    $scope.articles = [
      { id: 1, name: "Hamburger", price: 5.9 },
      { id: 2, name: "Burger", price: 7.9 },
      { id: 3, name: "Salad", price: 9.9 },
      { id: 4, name: "Bacon", price: 9.9 }
    ];
  })
  .controller("CartCtrl", function ($scope, Cart) {
    $scope.cart = Cart;
  });
