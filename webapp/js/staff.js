app.controller('StaffCtrl', function ($http, $scope) {
    request = $http.get('http://localhost/api/staff').then(
        function successCallback(response) {
            $scope.json = response.data;
    },
        function errorCallback(response){
            console.log("success");
            console.log(response);
    })
});
