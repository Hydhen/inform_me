app.controller('RulesCtrl', function ($http, $scope, $location) {
    request = $http.get('http://' + $location.host() + '/api/rules').then(
        function successCallback(response) {
            $scope.json = response.data;
    },
        function errorCallback(response){
            console.log("error");
            console.log(response);
    })
});
