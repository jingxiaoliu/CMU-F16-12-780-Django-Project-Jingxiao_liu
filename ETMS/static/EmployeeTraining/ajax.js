/**
 * Created by jingx on 11/25/2016.
 */
$(function(){

    $('#search').keyup(function(){
        $.ajax({
            type: "POST",
            url: "/employee/search/",
            data: {
                'search_text' : $('#search').val(),
                'csrfmiddlewaretoken': $("input[name=csrfmiddlewaretoken]").val()
            },
            success: searchSuccess,
            dataType: 'html'
        });
    });
});

function searchSuccess(data, textStatus, jqXHR)
{
    $('#search-results').html(data);
}