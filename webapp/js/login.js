app.controller('LoginCtrl', function ($scope, $http, $mdToast, $window, $location) {
    console.log("Login Ctrl");
    $scope.username = '';
    $scope.password = '';

    $scope.login = function () {
        data = {
            'username': this.username,
            'password': this.password
        };

        request = $http.post('http://' + $location.host() + '/api/login', data).then(
             function successCallback(response) {
                 console.log(response);
                 $scope.json = response.data;
                 if (response.data == 'Invalid login/password') {
                     console.log('Invalid login/password');
                     $mdToast.show(
                         $mdToast.simple()
                            .textContent('Invalid login/password')
                            .position('top right')
                            .hideDelay(2000)
                     );
                 }
                 else if (response.data == 'Logged in !') {
                     $window.location.href = '#/';
                     $window.location.reload();
                 }
             },
             function errorCallback(response){
                 console.log("error");
                 console.log(response);
             });
    }
});
