window.onload = () => {
    // Definir dados iniciais

    const trioMSN = {
        juntos: true,
        juntosMSN: {
            bigHeader: 'Esse é o trio MSN',
            smallHeader: 'Aqui o barça ganhava muitos títulos!',
            myParagraph: 'Messi, Neymar e Suarez felizes!!!',
            myImg: '../static/images/trio_msn.jpeg'
        },
        separadosMSN:{
            bigHeader: 'O trio MSN acabou!',
            smallHeader: 'Aqui o barça entrou em crise!',
            myParagraph: 'Messi, Neymar e Suarez tristes!!!',
            myImg: '../static/images/messi_suarez.jpg'
        }
    }

    // Atualizar dados

    const elemBigHeader = document.getElementById('big-header');
    const elemSmallHeader = document.getElementById('small-header');
    const elemMyParagraph = document.getElementById('my-paragraph');
    const elemMyImg = document.getElementById('my-img');

    function atualizaDados() {

        if(trioMSN.juntos){
            elemBigHeader.innerText = trioMSN.juntosMSN.bigHeader;
            elemSmallHeader.innerText = trioMSN.juntosMSN.smallHeader;
            elemMyParagraph.innerText = trioMSN.juntosMSN.myParagraph;
            elemMyImg.src = trioMSN.juntosMSN.myImg
        }else{
            elemBigHeader.innerText = trioMSN.separadosMSN.bigHeader;
            elemSmallHeader.innerText = trioMSN.separadosMSN.smallHeader;
            elemMyParagraph.innerText = trioMSN.separadosMSN.myParagraph;
            elemMyImg.src = trioMSN.separadosMSN.myImg
        }
    }

    atualizaDados();

    // Alterar humor

    const change = document.getElementById('change');
    change.addEventListener('click', () => {
        trioMSN.juntos = !trioMSN.juntos;

        atualizaDados();
    });

}
