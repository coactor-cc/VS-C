from sklearn.datasets import load_iris
from sklearn import tree

# ----------------数据准备----------------------------
iris = load_iris()  # 加载数据
# ---------------模型训练----------------------------------
clf = tree.DecisionTreeClassifier(criterion="gini",
                                  splitter="best",
                                  max_depth=None,
                                  min_samples_split=2,
                                  min_samples_leaf=1,
                                  min_weight_fraction_leaf=0.,
                                  max_features=None,
                                  random_state=None,
                                  max_leaf_nodes=None,
                                  min_impurity_decrease=0.,
                                  class_weight=None,
                                  ccp_alpha=0.0)  # sk-learn的决策树模型
clf = clf.fit(iris.data, iris.target)  # 用数据训练树模型构建()
r = tree.export_text(clf, feature_names=iris['feature_names'])  # 训练好的决策树
# ---------------模型预测结果------------------------
text_x = iris.data[[0, 1, 50, 51, 100, 101], :]
print(type(text_x))
pred_target_prob = clf.predict_proba(text_x)  # 预测类别概率
pred_target = clf.predict(text_x)  # 预测类别

# ---------------打印结果---------------------------
print("\n===模型======")
print(r)
print("\n===测试数据：=====")
print(text_x)
print("\n===预测所属类别概率：=====")
print(pred_target_prob)
print("\n===预测所属类别：======")
print(pred_target)


#