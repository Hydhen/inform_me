app.controller('HomeCtrl', function ($http, $scope) {
    request = $http.get('http://localhost/api/').then(
        function successCallback(response) {
            $scope.json = response.data;
    }).then(
        function errorCallback(response){
            console.log("success");
            console.log(response);
    })
});
