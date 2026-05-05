<?php
defined('ABSPATH') || exit;

function dijital_urunler_setup() {
    add_theme_support('title-tag');
    add_theme_support('html5', ['script', 'style', 'search-form', 'comment-form', 'comment-list', 'gallery', 'caption']);
}
add_action('after_setup_theme', 'dijital_urunler_setup');

function dijital_urunler_enqueue() {
    wp_enqueue_style(
        'dm-sans',
        'https://fonts.googleapis.com/css2?family=DM+Sans:ital,wght@0,300;0,400;0,500;0,600;0,700;0,800;0,900;1,400;1,700;1,800&display=swap',
        [],
        null
    );
    wp_enqueue_style('dijital-urunler', get_stylesheet_uri(), ['dm-sans'], '1.0.0');
}
add_action('wp_enqueue_scripts', 'dijital_urunler_enqueue');

// Remove the default WordPress admin bar on the front end (optional)
add_filter('show_admin_bar', '__return_false');
