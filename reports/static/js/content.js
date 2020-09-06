// 사이트 쿠키를 가져옵니다
function parse_cookies() {
    let cookies = {};
    if (document.cookie && document.cookie !== '') {
        document.cookie.split(';').forEach(function (c) {
            let m = c.trim().match(/(\w+)=(.*)/);
            if(m !== undefined) {
                cookies[m[1]] = decodeURIComponent(m[2]);
            }
        });
    }
    return cookies;
}

function validate() {
    let comment_textarea = document.getElementById('comment');
    let comment_text = comment_textarea.value;
    if (comment_text == '') {
        alert('발견 당시 상황을 설명해주세요');
        return false;
    }

    return true;
}

function save(user_id) {
    let cookies = parse_cookies();

    let comment_textarea = document.getElementById('comment');
    let comment_text = comment_textarea.value;
    if (comment_text == '') {
        return false;
    }

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
        images: images,
    }));

    return true;
}

let images = []
let csrftoken = parse_cookies()['csrftoken'];

Dropzone.autoDiscover = false;
$('#MultiFileUpload').dropzone({
    url: "http://127.0.0.1:8000/reports/fileupload/",
    crossDomain: false,
    paramName: "file",
    parallelUploads: 5,
    autoProcessQueue: true,
    filesizeBase: 1024,
    maxFilesize: 10000,
    dictRemoveFileConfirmation: null,
    init: function () {
        this.on("uploadprogress", function (file, progress, bytesSent) {
            progress = bytesSent / file.size * 100;
        });
        this.on("maxfilesexceeded", function (data) {
            let res = eval('(' + data.xhr.responseText + ')');
        });
        this.on("addedfile", function (file) {
            let removeButton = Dropzone.createElement("<a data-dz-remove " +
                "class='del_thumbnail btn btn-default'><span class='glyphicon glyphicon-trash'></span>삭제</a>");
            let _this = this;
            removeButton.addEventListener("click", function (e) {
                e.preventDefault();
                e.stopPropagation();
                _this.removeFile(file);
            });
            file.previewElement.appendChild(removeButton);
        });
        this.on("error", function (file, message) {

            console.log(message);
            this.removeFile(file);
        });
        this.on('sending', function (file, xhr, formData) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        });
        this.on('success', function() {
            let args = Array.prototype.slice.call(arguments);
            images.push(args[1]['images'][0]);
        });
        // this.on('removedfile', function() {
        //     let args = Array.prototype.slice.call(arguments);
        //     console.log(args);
        // })
    }
});

Dropzone.prototype.filesize = function (size) {
    filesizecalculation(size)
};

function filesizecalculation(size) {
    if (size < 1024 * 1024) {
        return "<strong>" + (Math.round(Math.round(size / 1024) * 10) / 10) + " KB</strong>";
    } else if (size < 1024 * 1024 * 1024) {
        return "<strong>" + (Math.round((size / 1024 / 1024) * 10) / 10) + " MB</strong>";
    } else if (size < 1024 * 1024 * 1024 * 1024) {
        return "<strong>" + (Math.round((size / 1024 / 1024 / 1024) * 10) / 10) + " GB</strong>";
    }
}