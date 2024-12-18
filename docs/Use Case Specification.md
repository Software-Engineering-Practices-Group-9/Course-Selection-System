---
title: Use Case Specification

---

# Use case diagram
![image](https://hackmd.io/_uploads/HJzVrbKJyg.png)

# Use case specification
## 開課
* 使用案例：開課

* 簡述：描述講課教授如何使用選課系統開課

* 參與行動者：講課教授
* 基本流程
    1. 輸入使用者的ID、密碼
    2. 驗證講課教授的使用者身分，成功登入
    3. 點選"新增課程"的按鈕
    4. 進入設定頁面
    5. 提示使用者輸入課程名稱(50字以內)、課程大綱(200字以內)、課程時間(範圍為星期一至星期五，第1節~第14節)、地點(20字以內)、選課人數上限(5至250人)，所有欄位皆為必塡。
    6. 使用者輸入課程大綱、課程名稱、課程時間、地點、選課人數上限
    7. 使用者確認無誤後，點選送出按鈕
    8. 彈出"確認送出?"的視窗，點選"送出"
    9. 新增一筆課程資料到主畫面的課程列表

* 替代流程
    2.1. 在流程第2步，假設檢驗是否為教授身分時，發生ID/密碼錯誤
    
        1. 提示ID/密碼錯誤
        2. 回到流程1
        3. 循環直到ID/密碼符合要求或選擇返回主畫面
    5.1. 在流程第5步，使用者輸入有1個欄位以上為空值。
    
        1. 移動頁面至未填寫的部分，提醒使用者
        2. 輸入符合要求或選擇返回主畫面
 
    5.2. 在流程第5步，使用者未選擇開課時段(星期一至星期五，第1節~第14節)。
        
        1. 彈窗提示使用者請至少選擇一個課程時間
        2. 回到流程4，保留原輸入設定
        3. 循環直到輸入符合要求或選擇返回主畫面
    5.3. 在流程第5步，使用者在選課人數輸入不在所提示的範圍(5至250人)。
        
        1. 彈窗提示使用者在選課人數上限欄位超出符合的範圍
        2. 回到流程4，保留原輸入設定
        3. 循環直到輸入符合要求或選擇返回主畫面
    5.4. 在流程第5步，使用者輸入的課程代碼已存在於課程列表
        
        1. 頁面提示使用者此課程代碼已存在
        2. 回到流程4，保留原輸入設定
        3. 循環直到輸入符合要求或選擇返回主畫面

    5.5. 在流程第5步，使用者輸入的學分數不在0-10學分之間

        1. 提示使用者學分數的值應在0-10學分之間
        2. 回到流程4，保留原輸入設定
        3. 循環直到輸入符合要求或選擇返回主畫面
    8.1. 在流程第8步，使用者點選取消按鈕
        
        1. 系統收到"取消"請求
        2. 回到流程4，保留原輸入設定

## 加選
* 使用案例：加選

* 簡述：描述學生如何使用選課系統加選課程

* 參與行動者：學生、系辦助教

* 基本流程
    1. 進入選課系統，輸入使用者的ID、密碼
    2. 系統驗證學生或系辦助教的使用者身分，成功登入
    3. 系統顯示選課頁面
    4. 使用者以課程代碼,課程名稱,教授,上課日期,上課節次搜尋欲加選的課程
    5. 系統顯示搜尋到的課程代碼、課程名稱、星期、節次、教室、人數上限、開課人員
    6. 使用者點擊加選按鈕
    7. 系統將使用者的學號或身分為"系辦助教"的使用者選擇的學號、以及欲加選的課程傳到課程資料處存端
    8. 系統顯示加選成功訊息

* 替代流程
    2.1. 於流程第2步，假設系統驗證使用者輸入的帳號密碼錯誤
    
        1. 提示ID/密碼錯誤
        2. 回到流程1
        3. 循環直到ID/密碼符合要求或選擇退出 
    5.1 於流程第5步，假如使用者輸入的課程名稱不存在
    
        1.課程搜尋結果顯示空白
        2.使用者重新輸入課程名稱
        3.進行流程第5步
    7.1 於流程第7步，假如某課程的以選人數已超出上限
        
        1.通知使用者此課程人數已滿
        2.拒絕使用者加選請求
        3.進行流程第6步
    7.2 於流程第7步，假如總學分已超過25
        
        1.通知使用者總學分已超過25
        2.拒絕使用者加選請求
        3.進行流程第6步
## 退選
* 使用案例：退選
* 簡述：描述學生或系辦助教如何使用課程系統退選
* 參與行動者：學生、系辦助教
* 基本流程
    1. 使用者進入選課系統，輸入使用者的ID、密碼
    2. 系統驗證學生或系辦助教的使用者身分，成功登入
    3. 系統顯示選課頁面
    4. 使用者以課程代碼,課程名稱,教授,上課日期,上課節次搜尋欲退選的課程
    5. 系統顯示搜尋到的課程代碼、課程名稱、星期、節次、教室、人數上限、開課人員
    6. 使用者點選退選按鈕
    7. 系統顯示視窗確認是否退選
    8. 系統檢查總學分是否會低於9學分或是為必修課程
    9. 系統將使用者欲退選課程的ID、名稱傳到後端資料庫進行核對
    10. 系統顯示退選成功訊息
* 替代流程
    2.1 於流程第2步，假設系統驗證使用者輸入的帳號密碼錯誤
    
        1. 顯示使用者重新輸入帳號或密碼
        2. 使用者重新輸入帳號或密碼
        3. 進行流程第2步
    7.1 於流程第7步，假設使用者取消退選
        
        4. 點選視窗"取消"按鈕
        5. 系統收到取消請求
        6. 回到流程第6步
    8.1 於流程第8步，若是總學分會低於9學分或是為必修課程
        
        7. 視窗顯示"最低修習學分需為9學分" 或 "此為必修課程，請聯絡系辦助教退選！"
        8. 系統拒絕退選請求
        9. 使用案例結束，退選失敗

## 停開
* 簡述：描述教務處人員如何使用選課系統停開課程
* 參與行動者：教務處人員
* 基本流程
    1. 進入選課系統，輸入ID、密碼
    2. 驗證教務處人員的使用者身分，成功登入
    3. 顯示所有的已開課程
    4. 於篩選條件查詢"已開課程"
    5. 送出查詢請求
    6. 顯示所有符合篩選條件的已開課程
    7. 透過手動瀏覽來選擇欲停開課程
    8. 於欲停開課程右方的選單點選"停開"
    9. 跳出確定的視窗
    10. 點選確定
    11. 收到選課系統的"停開課程成功"回覆
    12. 完成停開課程
* 替代流程
    2.1 於流程第2步，假設系統驗證使用者輸入的帳號密碼錯誤
    
        1. 顯示使用者重新輸入帳號或密碼
        2. 使用者重新輸入帳號或密碼
        3. 進行流程第2步
    5.1 若輸入的課程ID沒有匹配
    
        1. 重新輸入
    9.1 於流程第9步，假設使用者取消停開
        
        1. 點選視窗"取消"按鈕
        2. 系統收到取消請求
        3. 回到流程第8步

# Test cases
## 開課
### Test case 1
* 使用案例：開課
* 測試功能：系統會判斷使用者每個欄位(課程名稱、課程大綱、選課上限人數、課程時間、課程地點)都有填寫
* 系統初始狀態：選課系統會顯示每個欄位的標題、輸入格以及提示字。
* 測試動作：當使用者沒有輸入任何欄位的情況下，按下送出。
* 預期結果：系統不會將課程送出，將會顯示課程名稱、課程大綱、選課上限人數、課程時間、課程地點為必塡項目。

### Test case 2
* 使用案例：開課
* 測試功能：系統會判斷輸入的學分在0~10之間
* 系統初始狀態：選課系統會顯示每個欄位的標題、輸入格以及提示字。
* 測試動作：當使用者在課學分輸入不在0~10之間，其他欄位輸入皆無誤，按下送出。
* 預期結果：系統將會顯示課程學分需在0~10學分之間。

### Test case 3
* 使用案例：開課
* 測試功能：使用者按下送出，系統判斷所有欄位都無誤之後，課程新增成功
* 系統初始狀態：選課系統會顯示每個欄位的標題、輸入格以及提示字。
* 測試動作：當使用者輸入完所有欄位，並符合提示規範，按下送出。
* 預期結果：系統新增課程在課程列表。
## 加選
### Test case 1
* 使用案例：加選
* 測試功能：系統會在驗證使用者，發生密碼錯誤時，要求使用者重新輸入密碼
* 系統初始狀態：系統要求使用者輸入帳號密碼
* 測試動作：使用者輸入錯誤的密碼
* 預期結果：系統顯示請使用者重新輸入密碼並要求使用者重新輸入密碼 
### Test case 2
* 使用案例：加選
* 測試功能：系統會確認使用者輸入的課程名稱存不存在
* 系統初始狀態：使用者以課程名稱搜尋欲加選的課程
* 測試動作：使用者輸入不存在的課程名稱
* 預期結果：課程列表不會顯示任何課程資訊
### Test case 3
* 使用案例：加選
* 測試功能：當某課程的已選人數等於選課人數上限時系統會拒絕此次的加選請求
* 系統初始狀態：系統顯示搜尋到的課程名稱、課程期間、地點、人數上限、開課人員
* 測試動作：使用者點擊加選按鈕
* 預期結果：系統顯示此課程人數已滿
## 退選
### Test case 1
* 使用案例：退選
* 測試功能：學生成功退選課程
* 系統初始狀態：該課程為非必修，且目前學分在退選後不會低於9學分
* 測試動作：使用者點擊退選按鈕
* 預期結果：系統顯示退選成功訊息，並從課表中刪除該課程

### Test case 2
* 使用案例：退選
* 測試功能：系統確認修習課程是否為必修
* 系統初始狀態：該必修課程已列入學生課表
* 測試動作：學生點擊退選按鈕，嘗試退選必修課程
* 預期結果： 
    1. 系統視窗顯示"無法退選，該課程為必修，請聯絡系辦助教協助退選"
    2. 課程仍然會在課程列表中

### Test case 3
* 使用案例：退選
* 測試功能：系統確認總修習學分是否低於9學分
* 系統初始狀態：學生課程學分已達最低學分，退選該課程後將低於學分下限
* 測試動作：學生點擊退選按鈕，嘗試退選該課程
* 預期結果：
    1. 系統視窗顯示"無法退選，總學分不能低於9學分"
    2. 課程仍然會在課程列表中

## 停開
### Test case 1
* 測試功能：在篩選條件為"已開課程"下，返回的結果必須全部為已開課程
* 系統初始狀態：在"瀏覽課程"頁面，篩選條件為"已開課程"下
* 測試動作：輸入一個不存在的課程ID，送出查詢
* 預期結果：課程列表不會顯示任何課程資訊
### Test case 2
* 測試功能：收到選課系統的"停開課程成功"回覆後，課程有被確實停開
* 系統初始狀態：在"瀏覽課程"頁面，在篩選條件為"已開課程"下
* 測試動作：輸入剛剛停開的課程ID，送出查詢
* 預期結果：課程列表不會顯示任何課程資訊
### Test case 3
* 測試功能：只有教務處人員才能停開課程
* 系統初始狀態：在選課系統的登入頁面
* 測試動作：分別以教務處人員以外的使用者登入，在"瀏覽課程"頁面，瀏覽"已選課程"
* 預期結果：課程右方的選單不應該出現"停開"此一選項
