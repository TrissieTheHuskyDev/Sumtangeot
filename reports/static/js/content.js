// 사이트 쿠키를 가져옵니다
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
    // POST Method로 Request 열기
    request.open('POST', '', true);
    // CSRF 토큰을 설정
    request.setRequestHeader('X-CSRFToken', cookies['csrftoken']);
    // JSON 타입으로 전송
    request.setRequestHeader('Content-Type', 'application/json');
    // JSON 데이터 전송
    request.send(JSON.stringify({
        latitude: lat,
        longitude: lon,
        user_id: user_id,
        comment: comment_text,
        kor_name: kor_name_text,
    }));
}

Dropzone.options.fileDropzone = {
    url: 'http://127.0.0.1:8000/reports/upload',
    init: function() {
        var submitButton = document.querySelector("#btn-upload-file");
        var myDropzone = this;
        submitButton.addEventListener("click", function () {
            console.log("업로드");
            myDropzone.processQueue(); 
        });
    },
    autoProcessQueue: true,
    clickable: true,
    thumbnailHeight: 90,
    thumbnailWidth: 90,
    maxFiles: 5,
    maxFilesize: 10,
    parallelUploads: 99,
    addRemoveLinks: true,
    dictRemoveFile: '삭제',
    uploadMultiple: true,
};