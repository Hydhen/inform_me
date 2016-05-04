app.controller('StaffCtrl', function ($http, $scope, $location) {
    request = $http.get('http://' + $location.host() + '/api/staff').then(
        function successCallback(response) {
            $scope.json = response.data;
    },
        function errorCallback(response){
            console.log("success");
            console.log(response);
    })
});
