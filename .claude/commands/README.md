# 📚 Slash Commands - Learning Workflow

Commands để quản lý quá trình học tập với đánh giá chính xác.

## 🎯 Main Commands (Dùng hằng ngày)

### 1. `/start-lesson` - Khởi tạo bài học mới
```bash
/start-lesson CH3-Function_Calling/L4-Execute_Functions/Lesson.md
```

**Làm gì**:
- Đọc lesson requirements
- Phân tích test cases
- Chuẩn bị implementation skeleton
- Cập nhật memory với lesson start

**Khi nào dùng**: Trước khi bắt đầu coding

---

### 2. `/lesson-review` - Hoàn tất bài học ✨
```bash
/lesson-review CH3-L3_More_Declarations
```

**Làm gì** (TỰ ĐỘNG):
1. ✅ Phân tích bài học → Tạo JSON
2. ✅ Cập nhật CLAUDE.md với lesson summary
3. ✅ Cập nhật Neo4j memory
4. ✅ Tạo git commit với learning progress

**Khi nào dùng**: Sau khi pass ALL tests

---

## 🔧 Individual Tools (Advanced)

Nếu cần chạy từng bước riêng lẻ:

```bash
# Bước 1: Phân tích
/tools:1-analyze-lesson-concepts CH3-L3

# Bước 2: Cập nhật docs
/tools:2-document-learning {JSON}

# Bước 3: Cập nhật memory
/tools:3-update-learning-memory {JSON}

# Bước 4: Commit
/tools:4-commit-learning {JSON}
```

**📖 Chi tiết**: Xem `/tools/README.md`

---

## ⚠️ QUAN TRỌNG: Assessment Guidelines

**Trước khi dùng bất kỳ command nào**, đọc:
```
/tools/assessment-guidelines.md
```

**Key Rules**:
- ❌ KHÔNG dùng: "mastery", "expert", "advanced mastery"
- ✅ LUÔN dùng: "completed successfully", "can apply", "solid understanding"
- 📊 Đánh giá dựa trên BẰNG CHỨNG (test scores, working code)
- 🎓 Phản ánh GIAI ĐOẠN HỌC TẬP, không phải chuyên gia

---

## 📋 Typical Learning Flow

```
1. Nhận bài mới
   ↓
2. /start-lesson {LESSON_PATH}
   ↓
3. Code + Debug + Pass tests
   ↓
4. /lesson-review {LESSON_NAME}
   ↓
5. Push to GitHub
   ↓
6. Repeat!
```

---

## 🆘 Troubleshooting

### Command không chạy?
→ Kiểm tra file path có đúng không
→ Đảm bảo đang ở đúng working directory

### Terminology sai?
→ Đọc lại `assessment-guidelines.md`
→ Xem examples trong README files

### Memory bị duplicate?
→ Tools tự động check duplicate
→ Nếu vẫn bị, xóa observations cũ trước

---

## 📁 File Structure

```
.claude/commands/
├── README.md                    ← File này
├── start-lesson.md              ← Khởi tạo bài học
├── lesson-review.md             ← Main workflow (all-in-one)
└── tools/
    ├── README.md                ← Tool details
    ├── assessment-guidelines.md ← ⭐ CRITICAL READING
    ├── 1-analyze-lesson-concepts.md
    ├── 2-document-learning.md
    ├── 3-update-learning-memory.md
    └── 4-commit-learning.md
```

---

## 🎓 Philosophy

**Remember**:
- ✅ Hoàn thành bài học = Học được + Áp dụng được
- ❌ Hoàn thành bài học ≠ Thành thạo (Mastery)
- 🎯 Mastery = Nhiều năm kinh nghiệm + Chuyên môn sâu

**Goal**: Theo dõi tiến bộ CHÍNH XÁC, không thổi phồng thành tích.

---

**Happy Learning! 🚀**
