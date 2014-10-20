package com.example.location;

import java.io.OutputStream;
import java.util.ArrayList;

import android.os.Bundle;
import android.app.Activity;
import android.support.v4.view.ViewPager;
import android.support.v4.view.ViewPager.OnPageChangeListener;
import android.view.LayoutInflater;
import android.view.View;
import android.view.View.OnClickListener;
import android.widget.ImageView;
import android.widget.LinearLayout;
import android.widget.Toast;
import android.os.Bundle;
import android.app.Activity;
import android.content.Intent;
import android.content.SharedPreferences;
import android.content.SharedPreferences.Editor;
import android.support.v4.view.ViewPager;
import android.support.v4.view.ViewPager.OnPageChangeListener;
import android.view.LayoutInflater;
import android.view.View;
import android.view.View.OnClickListener;
import android.widget.ImageView;
import android.widget.LinearLayout;
import android.widget.Toast;

public class InitGuide extends Activity {
	// ����ViewPager����
	private ViewPager viewPager;
	// ����ViewPager������
	private ViewPagerAdapter vpAdapter;
	// ����һ��ArrayList�����View
	private ArrayList<View> views;
	// ����ͼƬ��Դ
	private static final int[] pics = { R.drawable.initguide1,
			R.drawable.initguide2, R.drawable.initguide3,
			R.drawable.initguide4, R.drawable.initguide5 };
	// �ײ�С���ͼƬ
	private ImageView[] points;
	// ��¼��ǰѡ��λ��
	private int currentIndex;
	private Editor editor;
	private OutputStream os;
	private SharedPreferences preferences;
	@Override
	protected void onCreate(Bundle savedInstanceState) {
		super.onCreate(savedInstanceState);
		setContentView(R.layout.initguide_main);
		preferences=getSharedPreferences("com.example.location_mypreferences", MODE_PRIVATE);
		String strCity=preferences.getString("ditCityPref", "����");
		if(preferences.getBoolean("firststart",true)){
		editor=preferences.edit();
		editor.putBoolean("firststart", false);
		editor.commit();
		initView();
		initData();
		}else{
			finish();
		startActivity(new Intent(InitGuide.this, MainActivity.class));
		}
	}

	/**
	 * ��ʼ�����
	 */
	private void initView() {
		// ʵ����ArrayList����
		views = new ArrayList<View>();
		// ʵ����ViewPager
		viewPager = (ViewPager) findViewById(R.id.viewpager);
		// ʵ����ViewPager������
		vpAdapter = new ViewPagerAdapter(views);
	}
	/**
	 * ��ʼ������
	 */
	private void initData() {
		LayoutInflater inflater = getLayoutInflater();

		for (int i = 0; i < pics.length; i++) {
			View v = inflater.inflate(R.layout.item_view, null);
			ImageView image = (ImageView) v.findViewById(R.id.image);
			image.setImageResource(pics[i]);
			views.add(v);
		}

		// ��������
		viewPager.setAdapter(vpAdapter);
		// ���ü���
		viewPager.setOnPageChangeListener(new pageListener());

		// ��ʼ���ײ�С��
		initPoint();
	}

	/**
	 * ��ʼ���ײ�С��
	 */
	private void initPoint() {
		LinearLayout linearLayout = (LinearLayout) findViewById(R.id.ll);

		points = new ImageView[pics.length];

		// ѭ��ȡ��С��ͼƬ
		for (int i = 0; i < pics.length; i++) {
			// �õ�һ��LinearLayout�����ÿһ����Ԫ��
			points[i] = (ImageView) linearLayout.getChildAt(i);
			// Ĭ�϶���Ϊ��ɫ
			points[i].setEnabled(true);
			// ��ÿ��С�����ü���
			points[i].setOnClickListener(new pointListener());
			// ����λ��tag������ȡ���뵱ǰλ�ö�Ӧ
			points[i].setTag(i);
		}

		// ���õ���Ĭ�ϵ�λ��
		currentIndex = 0;
		// ����Ϊ��ɫ����ѡ��״̬
		points[currentIndex].setEnabled(false);
	}

	private class pageListener implements OnPageChangeListener {

		/**
		 * ������״̬�ı�ʱ����
		 */
		@Override
		public void onPageScrollStateChanged(int arg0) {
			// TODO Auto-generated method stub

		}

		/**
		 * ����ǰҳ�汻����ʱ����
		 */
		@Override
		public void onPageScrolled(int arg0, float arg1, int arg2) {
			// TODO Auto-generated method stub

		}

		/**
		 * ���µ�ҳ�汻ѡ��ʱ����
		 */
		@Override
		public void onPageSelected(int position) {
			// ���õײ�С��ѡ��״̬
			setCurDot(position);
		}

	}

	private class pointListener implements OnClickListener {
		/**
		 * ͨ������¼����л���ǰ��ҳ��
		 */
		@Override
		public void onClick(View v) {
			int position = (Integer) v.getTag();
			setCurView(position);
			setCurDot(position);
		}

	}

	/**
	 * ���õ�ǰҳ���λ��
	 */
	private void setCurView(int position) {
		if (position < 0 || position >= pics.length) {
			return;
		}
		viewPager.setCurrentItem(position);
	}

	/**
	 * ���õ�ǰ��С���λ��
	 */
	private void setCurDot(int positon) {
		if (positon < 0 || positon > pics.length - 1 || currentIndex == positon) {
			return;
		}
		points[positon].setEnabled(false);
		points[currentIndex].setEnabled(true);
		currentIndex = positon;
	}

	public void Init(View v) {
		startActivity(new Intent(InitGuide.this, MainActivity.class));
		Toast.makeText(this, "��ӭʹ��", 1).show();

	}

}
