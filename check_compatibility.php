<<<<<<< HEAD
<?php
header('Content-Type: application/json');

$cpu_id = isset($_GET['cpu']) ? (int)$_GET['cpu'] : 0;
$mobo_id = isset($_GET['mobo']) ? (int)$_GET['mobo'] : 0;
$gpu_id = isset($_GET['gpu']) ? (int)$_GET['gpu'] : 0;

// MOCK DATABASE LOGIC
// In a real project, you would do: SELECT socket FROM cpus WHERE id = $cpu_id
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

// Initialize response array
$response = [
    'socketCompatible' => false,
    'bottleneck' => false,
    'gpuMessage' => ''
];

// Validate if items exist
if (isset($mock_cpus[$cpu_id]) && isset($mock_mobos[$mobo_id]) && isset($mock_gpus[$gpu_id])) {
    $selected_cpu = $mock_cpus[$cpu_id];
    $selected_mobo = $mock_mobos[$mobo_id];
    $selected_gpu = $mock_gpus[$gpu_id];

    // Check Socket Compatibility
    if ($selected_cpu['socket'] === $selected_mobo['socket']) {
        $response['socketCompatible'] = true;
    }

    // Check CPU and GPU pairing (simple logic: if scores differ too much = bottleneck)
    $score_difference = abs($selected_cpu['performance_score'] - $selected_gpu['performance_score']);
    
    if ($score_difference > 15) {
        $response['bottleneck'] = true;
        $response['gpuMessage'] = "The CPU might bottleneck the GPU, or vice versa. Consider a more balanced pair.";
    } else {
        $response['gpuMessage'] = "This is a well-balanced build.";
    }
}

echo json_encode($response);
=======
<?php
header('Content-Type: application/json');

$cpu_id = isset($_GET['cpu']) ? (int)$_GET['cpu'] : 0;
$mobo_id = isset($_GET['mobo']) ? (int)$_GET['mobo'] : 0;
$gpu_id = isset($_GET['gpu']) ? (int)$_GET['gpu'] : 0;

// MOCK DATABASE LOGIC
// In a real project, you would do: SELECT socket FROM cpus WHERE id = $cpu_id
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

// Initialize response array
$response = [
    'socketCompatible' => false,
    'bottleneck' => false,
    'gpuMessage' => ''
];

// Validate if items exist
if (isset($mock_cpus[$cpu_id]) && isset($mock_mobos[$mobo_id]) && isset($mock_gpus[$gpu_id])) {
    $selected_cpu = $mock_cpus[$cpu_id];
    $selected_mobo = $mock_mobos[$mobo_id];
    $selected_gpu = $mock_gpus[$gpu_id];

    // Check Socket Compatibility
    if ($selected_cpu['socket'] === $selected_mobo['socket']) {
        $response['socketCompatible'] = true;
    }

    // Check CPU and GPU pairing (simple logic: if scores differ too much = bottleneck)
    $score_difference = abs($selected_cpu['performance_score'] - $selected_gpu['performance_score']);
    
    if ($score_difference > 15) {
        $response['bottleneck'] = true;
        $response['gpuMessage'] = "The CPU might bottleneck the GPU, or vice versa. Consider a more balanced pair.";
    } else {
        $response['gpuMessage'] = "This is a well-balanced build.";
    }
}

echo json_encode($response);
>>>>>>> df56ab640c4fba47c9149cb50687d306a3dcea22
?>