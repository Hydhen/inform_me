app.controller('ContactCtrl', function ($http, $scope, $location) {
    request = $http.get('http://' + $location.host() + '/api/contact').then(
        function successCallback(response) {
            $scope.json = response.data;
    },
        function errorCallback(response){
            console.log("error");
            console.log(response);
    })
});
