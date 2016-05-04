
app.controller('ProjectCtrl', function ($http, $scope, $mdDialog, $mdMedia, $location) {
    request = $http.get('http://' + $location.host() + '/api/project').then(
        function successCallback(response) {
            $scope.json = response.data;
    },
        function errorCallback(response){
            console.log("error");
            console.log(response);
    });

    $scope.showDialog = function(id) {
        $mdDialog.show({
            controller: DialogController,
            templateUrl: 'project_tmpl.html',
            clickOutsideToClose: true,
            locals: {
                id: id
            }
        });
    };
});

function DialogController($http, $scope, $mdDialog, $location, id) {
    $scope.id = id;
    console.log("lol");
    request = $http.get('http://' + $location.host() + '/api/project/' + id).then(
        function successCallback(response) {
            $scope.json = response.data;
            console.log($scope.json.created);
            console.log(response.data);
    },
        function errorCallback(response){
            console.log("error");
            console.log(response);
    });

}
