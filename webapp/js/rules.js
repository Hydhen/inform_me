app.controller('RulesCtrl', function ($http, $scope) {
    request = $http.get('http://localhost/api/rules').then(
        function successCallback(response) {
            $scope.json = response.data;
    },
        function errorCallback(response){
            console.log("success");
            console.log(response);
    })
});
