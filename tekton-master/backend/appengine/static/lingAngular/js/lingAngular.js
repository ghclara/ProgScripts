var linguagemmodulo=angular.module('linguagemmodulo',[]);

linguagemmodulo.directive('linguagemform', function() {
    return{
    restrict:'E',
    templateUrl:'/static/lingAngular/html/linguagem_form.html'
    }
});
