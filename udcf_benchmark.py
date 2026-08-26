% UDCF Reproducibility Script for Tables 1-4
% Author: Clifford Yeboah et al.

% 1. Load Table 1 Data
% Columns: Dermis, HDPE, Al6061, A36
raw_data = [
    1.24, 1.38, 0.86, 0.94;
    1.02, 1.45, 0.89, 0.89;
    1.18, 1.40, 0.90, 0.91;
    1.05, 1.47, 0.87, 0.93;
    1.21, 1.40, 0.88, 0.93
];

% 2. Calculate Statistics (Reproducing Table 1)
means = mean(raw_data);
stds = std(raw_data);
cv = (stds ./ means) * 100;

fprintf('--- Table 1 Statistical Verification ---\n');
fprintf('Material: Dermis | Mean: %.2f | Std: %.3f | CV: %.2f%%\n', means(1), stds(1), cv(1));
fprintf('Material: HDPE   | Mean: %.2f | Std: %.3f | CV: %.2f%%\n', means(2), stds(2), cv(2));

% 3. UDCF Formula Verification (Reproducing Table 4)
% η = kY * ( (m * v^2) / (2 * d * tau * A) )
calculate_eta = @(kY, m, v, d, tau, A) kY * ((m * v^2) / (2 * d * tau * A));

% Example: Axe vs Pine Wood
eta_axe = calculate_eta(0.40, 2.5, 12.0, 0.05, 8.0e6, 5.0e-5);
fprintf('\n--- Table 4 Formula Verification ---\n');
fprintf('Axe vs Pine Wood η: %.2f (Expected: 3.60)\n', eta_axe);
