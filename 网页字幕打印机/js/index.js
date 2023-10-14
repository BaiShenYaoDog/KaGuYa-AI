// 用于保存当前正在显示的动画的引用
let currentAnimation;
let isHiding = false;
let hideSubtitle_Timeout;
// 隐藏字幕的动画时间
let hide_time = 1000;
// 显示完毕多久后隐藏字幕
let show_over_hide_time = 5000;
// 单个字符显示耗时
let single_char_show_time = 300;
// 渐变显示耗时
let gradient_show_time = 500;
// 显示框字体
let subtitle_font_family = '微软雅黑';

const socket = io.connect('http://localhost:5500');

socket.on('message', function(data) {
    showSubtitle(data.content);
});

// 显示文本内容的函数 
function showSubtitle(text) {
    show_over_hide_time = text.length*single_char_show_time

    // 清空之前的文本内容
    clearSubtitle();

    // 停止当前的动画（如果有）
    if (currentAnimation) {
        cancelAnimationFrame(currentAnimation);
    }

    clearTimeout(hideSubtitle_Timeout);

    const subtitleDiv = document.getElementById("subtitle");
    subtitleDiv.innerText = text;
    subtitleDiv.style.opacity = 0;
    subtitleDiv.style.transition = `opacity ${gradient_show_time / 1000}s ease-in`;

    setTimeout(() => {
        subtitleDiv.style.opacity = 1;
    }, 100); // 延迟 100 毫秒以确保渐变效果有效

    hideSubtitle_Timeout = setTimeout(() => {
        hideSubtitle(hide_time);
    }, show_over_hide_time + gradient_show_time);
}

// 清空内容的函数
function clearSubtitle() {
    const subtitleDiv = document.getElementById("subtitle");
    subtitleDiv.innerText = "";
}

// 渐变隐藏的函数
function hideSubtitle(fadeOutDuration) {
    if (isHiding) {
        return; // 如果已经在隐藏过程中，不要再次触发
    }
    isHiding = true;

    const subtitleDiv = document.getElementById("subtitle");
    subtitleDiv.style.transition = `opacity ${fadeOutDuration}ms`;
    subtitleDiv.style.opacity = 0;

    setTimeout(() => {
        clearSubtitle();
        isHiding = false;
    }, fadeOutDuration);
}