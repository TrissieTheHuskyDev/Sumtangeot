function parse_cookies() {
    var cookies = {};
    if (document.cookie && document.cookie !== '') {
        document.cookie.split(';').forEach(function (c) {
            var m = c.trim().match(/(\w+)=(.*)/);
            if(m !== undefined) {
                cookies[m[1]] = decodeURIComponent(m[2]);
            }
        });
    }
    return cookies;
}

function save(user_id) {
    let cookies = parse_cookies();

    let comment_textarea = document.getElementById('comment');
    let comment_text = comment_textarea.value;

    let kor_name_input = document.getElementById('kor-name');
    let kor_name_text = kor_name_input.value;

    let request = new XMLHttpRequest();
    request.open('POST', '', true);
    request.setRequestHeader('X-CSRFToken', cookies['csrftoken']);
    request.setRequestHeader('Content-Type', 'application/json');
    request.send(JSON.stringify({
        latitude: lat,
        longitude: lon,
        user_id: user_id,
        comment: comment_text,
        kor_name: kor_name_text,
    }));
}