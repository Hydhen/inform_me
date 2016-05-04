app.controller('HomeCtrl', function ($http, $scope, $location) {
    request = $http.get('http://' + $location.host() + '/api/').then(
        function successCallback(response) {
            $scope.json = response.data;
    },
        function errorCallback(response){
            console.log("success");
            console.log(response);
    })
});
