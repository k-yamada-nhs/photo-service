var target = null;

window.onload = function() {
    
    var drag = document.getElementById('drag');
    var drop = document.getElementById('drop');
    
    // drag側
    drag.addEventListener('dragstart', function(e){
        target = e.target;
    }, false);
    
    
    drag.addEventListener('drag', function(){
        // 非表示
        drag.style.display = 'none';  
    }, false);
    
    // drop側
    document.addEventListener('dragover', function(e){
        e.preventDefault(); 
    }, false);
    
    document.addEventListener('drop', function(e){
        e.preventDefault();
        if (e.target.id == 'drop'){
            e.target.appendChild(target);
        }
        // 表示
        drag.style.display = 'block';

    }, false);
    
} 
