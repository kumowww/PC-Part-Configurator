<?php
header('Content-Type: application/json');

$cpu_id = filter_input(INPUT_GET, 'cpu', FILTER_VALIDATE_INT, ['options' => ['min_range' => 1]]) ?: 0;
$mobo_id = filter_input(INPUT_GET, 'mobo', FILTER_VALIDATE_INT, ['options' => ['min_range' => 1]]) ?: 0;
$gpu_id = filter_input(INPUT_GET, 'gpu', FILTER_VALIDATE_INT, ['options' => ['min_range' => 1]]) ?: 0;

$mock_cpus = [
    1 => ['name' => 'AMD Ryzen 5 5600X', 'socket' => 'AM4', 'performance_score' => 80],
    2 => ['name' => 'Intel Core i5-12400F', 'socket' => 'LGA1700', 'performance_score' => 85]
];

$mock_mobos = [
    1 => ['name' => 'MSI B550 TOMAHAWK', 'socket' => 'AM4'],
    2 => ['name' => 'ASUS PRIME Z690-P', 'socket' => 'LGA1700']
];

$mock_gpus = [
    1 => ['name' => 'NVIDIA RTX 3060', 'performance_score' => 75],
    2 => ['name' => 'AMD Radeon RX 6700 XT', 'performance_score' => 85]
];

$response = [
    'socketCompatible' => false,
    'bottleneck' => false,
    'gpuMessage' => ''
];

if (array_key_exists($cpu_id, $mock_cpus) && array_key_exists($mobo_id, $mock_mobos) && array_key_exists($gpu_id, $mock_gpus)) {
    $selected_cpu = $mock_cpus[$cpu_id];
    $selected_mobo = $mock_mobos[$mobo_id];
    $selected_gpu = $mock_gpus[$gpu_id];

    if ($selected_cpu['socket'] === $selected_mobo['socket']) {
        $response['socketCompatible'] = true;
    }

    $score_difference = abs($selected_cpu['performance_score'] - $selected_gpu['performance_score']);

    if ($score_difference > 15) {
        $response['bottleneck'] = true;
        $response['gpuMessage'] = "The CPU might bottleneck the GPU, or vice versa. Consider a more balanced pair.";
    } else {
        $response['gpuMessage'] = "This is a well-balanced build.";
    }
}

echo json_encode($response);