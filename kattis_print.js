document.querySelector('.header').remove()
document.querySelector('#footer').remove()
document.querySelector('.col-xs-3').remove()
document.querySelector('.col-xs-9').style.width = '100%'
document.querySelector('.container').style.width = '90%'
document.querySelector('.container').style.margin = '0px 5%'
document.querySelector('.page-content.single').style.margin = '0px auto'
document.querySelectorAll('img').forEach((x) => {
    x.style.padding = '14px'
})
window.print()
