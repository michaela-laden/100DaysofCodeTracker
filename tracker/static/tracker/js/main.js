document.addEventListener('DOMContentLoaded', ()=>{
    const grid = document.querySelector('.grid');
    const width = 7;
    const height = 14.2;
    const squares = [];


    function createBoard(){
        for (let i = 0; i < width*height; i++){
            const square = document.createElement('div');
            square.setAttribute('id', i);
            square.innerHTML= (i+1);
            if (i<=25) {
                square.setAttribute('class', 'box-1');
            } else if (i>25 && i<=50){
                square.setAttribute('class', 'box-2');
            } else if (i>50 && i<=75){
                square.setAttribute('class', 'box-3');
            } else if (i>75 && i<=98){
                square.setAttribute('class', 'box-4');
            } else {
                square.setAttribute('class', 'box-5');
            }
            grid.appendChild(square);
            squares.push(square);
        }
    }


    createBoard();

})