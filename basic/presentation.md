# 2020-09-06 初心者グループ
オンラインコードリファクタリング リターンズ

１）リファクタリング（旧仕様と同じ動きを数ること）
２）テストケース（テスト名・意味・デスクリプション）→Readable（テスト命名規約）
３）Pytestは部分実行可
４）テストツールはどれがBEST？

=====
戻り値が最初は
　add, sub = add(num1, num2), sub(num1, num2)
短くてわかりやすいけど関数名と被って混乱するかも
add_result, sub_result = add(num1, num2), sub(num1, num2)

=====
必ずしも１行がわかりやすいわけではない

add, sub = add(num1, num2), sub(num1, num2)
add(num1, num2)→エラーになる

add_result = add(num1, num2)
sub_result = sub(num1, num2)

=====
add, sub = add(num1, num2), sub(num1, num2)
add(num1, num2)→エラーになる
   
=====
==== UnitTest 実行結果

    (calc) ~/w/c/b/calc ❯❯❯ pipenv run pytest                                                     ✘ 2 master ✱ ◼
============================================ test session starts ============================================
platform darwin -- Python 3.8.2, pytest-6.0.1, py-1.9.0, pluggy-0.13.1
rootdir: /Users/tae/works/code-refactor-discussion/basic/calc
collected 4 items                                                                                           

test_calc.py ....                                                                                     [100%]

============================================= 4 passed in 0.02s =============================================
%                                                                                                
(calc) ~/w/c/b/calc ❯❯❯                                                                         m
(calc) ~/w/c/b/calc ❯❯❯                                                                         m
(calc) ~/w/c/b/calc ❯❯❯                                                                         master ✱ ◼