
app.controller('ProjectCtrl', function ($http, $scope, $mdDialog, $mdMedia) {
    request = $http.get('http://localhost/api/project').then(
        function successCallback(response) {
            $scope.json = response.data;
    },
        function errorCallback(response){
            console.log("success");
            console.log(response);
    });

    $scope.showDialog = function(id) {
        $mdDialog.show({
            controller: DialogController,
            templateUrl: 'project_template.html',
            clickOutsideToClose: true,
            locals: {
                id: id
            }
        });
    };
});

function DialogController($http, $scope, $mdDialog, id) {
    $scope.id = id;
    console.log("lol");
    request = $http.get('http://localhost/api/project/' + id).then(
        function successCallback(response) {
            console.log("lol");
            $scope.json = response.data;
            console.log("lol");
    },
        function errorCallback(response){
            console.log("success");
            console.log(response);
    });

}

/*        var useFullScreen = ($mdMedia('sm') || $mdMedia('xs'))  && $scope.customFullscreen;
$mdDialog.show({
controller: DialogController,
templateUrl: 'dialog1.tmpl.html',
parent: angular.element(document.body),
targetEvent: ev,
clickOutsideToClose:true,
fullscreen: useFullScreen
})
.then(function(answer) {
$scope.status = 'You said the information was "' + answer + '".';
}, function() {
$scope.status = 'You cancelled the dialog.';
});
$scope.$watch(function() {
return $mdMedia('xs') || $mdMedia('sm');
}, function(wantsFullScreen) {
$scope.customFullscreen = (wantsFullScreen === true);
});
*/
