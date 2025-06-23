$(document).ready(function () {
    $('a.external').each(function( index, elem ) {
        var str = $(elem).html();
        $(elem).html(str + '<i class="icon icon-external-link" aria-hidden="true"></i><span class="sr-only-no-select">&nbsp;(external link opens in a new tab)&nbsp;</span>');
        $(elem).attr('target', '_blank');
        $(elem).attr('rel', 'noopener');
    });
});
